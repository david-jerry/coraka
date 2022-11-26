/** @type {import('tailwindcss').Config} */
const Path = require("path");
const pwd = process.env.PWD;

const projectPaths = [
  Path.join(pwd, "./coraka/templates/**/*.html"),
  Path.join(pwd, "../coraka/templates/**/*.html"),
  Path.join(pwd, "../../coraka/templates/**/*.html"),
  Path.join(pwd, "./node_modules/flowbite/**/*.js" )
  // add js file paths if you need
];

const contentPaths = [...projectPaths];
console.log(`tailwindcss will scan ${contentPaths}`);

const defaultTheme = require('tailwindcss/defaultTheme');
// const plugin = require('tailwindcss/plugin');


module.exports = {
  content: contentPaths,
  theme: {
    extend: {
      screens: {
        xxs: '325px',
        ...defaultTheme.screens
      },
      fontSize: {
        xxs: '0.55rem',
        s: "0.65rem",
      },
      fontFamily: {
        "poppins": ["'Poppins'", "sans-serif"],
        "p1": ["'Poiret One'", "cursive"],
        "vpro": ["'Be Vietnam Pro'", "sans-serif"],
        "dpuff": ["'DynaPuff'", "cursive"],
        "raleway": ["'Raleway'", "Montserrat", "sans-serif"],
        "slab": ["'Antic Slab'", "serif"]
      },
      colors: {
        light: '#E2E2E2',
        dark: '#15182b',
        debug: "#636363",
        warning: '#F7C300',
        primary: "#1070CA",
        info: "#1070CA",
        danger: '#FF0000',
        success: "#1adcca",
      },
      keyframes: {
        wiggle: {
            '0%, 100%': { transform: 'rotate(-9deg)' },
            '50%': { transform: 'rotate(9deg)' },
        },
      },
      animation: {
        wiggle: 'wiggle 1s ease-in-out infinite',
        'wiggle-slow': 'wiggle 2s linear infinite',
        'ping-slow': 'ping 1s linear infinite',
        'ping-slower': 'ping 2s linear infinite',
        'spin-slow': 'spin 2s linear infinite',
        'spin-slower': 'spin 3s linear infinite',
        'bounce-slow': 'bounce 3s linear infinite',
      }
    },
  },
  variants: {
    extend: {},
    scrollBar: ["rounded"],
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/aspect-ratio'),
    require('tailwind-scrollbar-hide'),
    require('tailwind-scrollbar'),
    require("daisyui"),
    require('flowbite/plugin')
  ],
};
