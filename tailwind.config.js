/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
    'apps/*/templates/*/*.html',
    'apps/*/templates/*.html',

    // Flowbite
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        'primary-color': '#0b1b4b',
        'primary-color2':'#FB9129',
        'button-hover':'#0e0761',
        'sec-color': 'e78e26',
        'pry-font-color': '#948894',
        'heading-color': '#6b6a94'
      },
      screens: {
        'xsm': '520px'
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
