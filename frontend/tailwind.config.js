module.exports = {
  purge: { content: ["./public/**/*.html", "./src/**/*.vue"] },
  darkMode: "class", // or 'media' or 'class'
  theme: {
    fontFamily: {
      rubik: ["Rubik", "sans-serif"],
    },
    extend: {
      colors: {
        "dark-primary": "#3C424B",
        "dark-secondary": "#282C37",
        "dark-accent": "#00FFE3",

        "light-primary": "#FFFFFF",
        "light-secondary": "#F5F8FB",
        "light-accent": "#00FFE3",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
