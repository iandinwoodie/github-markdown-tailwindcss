# github-markdown-tailwindcss
Replicate GitHub Flavored Markdown with Tailwind CSS components

## Note for Users

The `markdown` rules defined in the stylesheet are currently nested for use with `postcss-nesting`. To use this stylesheet without nesting the conversion is quite simple:

```css
/* Nested */
.markdown {
  & p {
    @apply text-base;
  }
}

/* Unnested */
.markdown p {
  @apply text-base;
}
```

I will unnest the stylesheet this evening (8/9/2019) so that its use in its default state isn't tied to a specific workflow. For those who use nesting I will provide a script to generate a nested stylesheet.
