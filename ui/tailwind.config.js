import catppuccin from "@catppuccin/daisyui";

module.exports = {
  content: ["./src/**/*.{js,ts}", "index.html"],
  plugins: [require("daisyui")],
  daisyui: {
    // The top value of this array will be used as the default theme
    // You can use https://github.com/saadeghi/theme-change to switch between themes
    themes: [
      // You can simply select a catppuccin flavor with sane default colors
      catppuccin("mocha"),
    ],
  },
};
