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
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
