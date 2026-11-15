# frozen_string_literal: true

require "cgi"

# Builds a table of contents from the headings Kramdown already rendered.
# The Markdown files stay the source of the text and of the heading ids.
module TocFilter
  def extract_toc(html)
    items = []
    html.to_s.scan(%r{<h2\b([^>]*)>(.*?)</h2>}m) do |attrs, inner|
      id = attrs[/\sid=["']([^"']+)["']/, 1] || attrs[/\Aid=["']([^"']+)["']/, 1]
      next if id.nil? || id.empty?

      text = CGI.unescapeHTML(inner.gsub(/<[^>]+>/, "")).gsub(/\s+/, " ").strip
      next if text.empty?

      items << { "id" => id, "text" => text }
    end
    items
  end
end

Liquid::Template.register_filter(TocFilter)
