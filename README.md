# github-markdown-tailwindcss

⛵ Replicate GitHub Flavored Markdown with Tailwind CSS components

## Usage

To use, include the provided style sheet (`markdown.css`) and add the `markdown`
class to any element that you wish to render as Github Flavored Markdown (GFM).

### Example

```html
<!-- Rendered in default Tailwind style -->
<h1>Header</h1>

<!-- Rendered in GFM style -->
<h1 class="markdown">Header</h1>
```

## Working with Hugo

You can use this style sheet to style your generated Hugo content. To do so,
wrap your content with an element that contains the `markdown` class.

### Example

```html
<div class="markdown">
  {{ .Content }}
</div>
```

## Nesting

For those of you who wish to have the class rules nested I have provided a
simple python script (`nest.py`) to generate a style sheet with nesting
(`markdown-nested.css`). The nesting script just applies a very simple
reformatting.

### Using the Nest Script

```bash
python nest.py
```
