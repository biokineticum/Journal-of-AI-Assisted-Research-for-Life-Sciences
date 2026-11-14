# frozen_string_literal: true

# Rewrites relative links to Markdown files after Kramdown has parsed them.
#
# jekyll-relative-links scans the raw Markdown with a regular expression.
# That expression treats a task-list checkbox ("- [ ]") or a placeholder
# such as "[yes / no / unknown]" on the same line as the start of the link,
# and it corrupts the policies. Rewriting href attributes in the HTML
# avoids that.

require "cgi"

module RewriteMarkdownLinks
  class << self
    def rewrite_site_page(page)
      return if page.output.nil? || page.output.empty?

      urls = page.site.data["md_page_urls"] ||= build_index(page.site)
      output = page.output.dup
      output.gsub!(/\bhref=(["'])([^"']+)\1/) do
        quote = Regexp.last_match(1)
        href = Regexp.last_match(2)
        rewritten = rewrite_href(href, page.relative_path, urls, page.site)
        %(href=#{quote}#{rewritten}#{quote})
      end
      page.output = output
    end

    def build_index(site)
      site.pages.each_with_object({}) do |other, map|
        map[other.relative_path] = public_url(site, other.url)
      end
    end

    def public_url(site, url)
      base = site.baseurl.to_s.sub(%r{/\z}, "")
      return url if base.empty? || url.start_with?("#{base}/") || url == base

      "#{base}#{url}"
    end

    def rewrite_href(href, source, urls, site)
      raw = CGI.unescapeHTML(href)
      return href if raw.start_with?("http://", "https://", "mailto:", "#", "//", "data:")

      path, fragment = raw.split("#", 2)
      path, query = path.split("?", 2)
      return href unless path.downcase.end_with?(".md")
      return href if path.start_with?("/")

      target = normalize(source, path)
      destination = urls[target]
      if destination.nil?
        raise "Unresolved Markdown link '#{href}' in #{source} (looked for #{target})"
      end

      destination += "?#{query}" if query && !query.empty?
      destination += "##{fragment}" if fragment && !fragment.empty?
      destination
    end

    def normalize(source, relative)
      dir = File.dirname(source)
      parts = dir == "." ? [] : dir.split("/")
      relative.split("/").each do |part|
        next if part.empty? || part == "."

        if part == ".."
          parts.pop
        else
          parts << part
        end
      end
      parts.join("/")
    end
  end
end

Jekyll::Hooks.register :pages, :post_render do |page|
  RewriteMarkdownLinks.rewrite_site_page(page)
end
