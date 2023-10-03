/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./surveyapp/templates/**/*.html',
          './node_modules/flowbite/**/*.js'
],
  theme: {
    extend: {},
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
  },
  plugins: [
    require('flowbite/plugin'),
  
      require('flowbite-typography'),
  ],
}

