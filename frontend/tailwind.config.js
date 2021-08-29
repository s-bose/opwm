module.exports = {
  purge: { content: ["./public/**/*.html", "./src/**/*.vue"] },
  darkMode: "class", // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        "dark-primary": "#3C424B",
        "dark-secondary": "#282C37",
        "dark-accent": "#00FFE3",

        "light-primary": "#FFFFFF",
        "light-secondary": "#F5F8FB",
        "light-accent": "#F5F8FB",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
