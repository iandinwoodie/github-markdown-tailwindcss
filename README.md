<h1 align="center">github-markdown-tailwindcss</h1>

<p align="center">
⛵ Replicate GitHub Flavored Markdown with Tailwind CSS components
</p>

## 🔩 Usage

To use, include the provided style sheet (`markdown.css`) and add the `markdown`
class to any element that you wish to render as Github Flavored Markdown (GFM).

### Example

```html
<!-- Rendered in default Tailwind style -->
<h1>Header</h1>

<!-- Rendered in GFM style -->
<h1 class="markdown">Header</h1>
```
## ![favicon-32x32](https://user-images.githubusercontent.com/20260845/62817975-cd02ea00-bb0d-11e9-9553-077e509cf3f5.png)&nbsp;Working with Hugo

You can use this style sheet to style your generated Hugo content. To do so,
wrap your content with an element that contains the `markdown` class.

### Example

```html
<div class="markdown">
  {{ .Content }}
</div>
```

## 🕊️ Nesting

For those of you who wish to have the class rules nested I have provided a
simple python script (`nest.py`) to generate a style sheet with nesting
(`markdown-nested.css`). The nesting script just applies a very simple
reformatting.

### Using the Nest Script

```bash
python nest.py
```

## 👬 Contribution

- Report issues
- Open pull request with improvements
- Spread the word
