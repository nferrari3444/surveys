/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./surveyapp/templates/**/*.html',
          './node_modules/flowbite/**/*.js'
],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
  
      require('flowbite-typography'),
  ],
}

