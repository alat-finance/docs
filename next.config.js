const withNextra = require('nextra')({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.tsx',
})

module.exports = withNextra({
  i18n:{
    locales: ['en', 'zh', 'id', 'hi', 'tr', 'ru', 'fr', 'pt', 'es', 'vi', 'ar'],
    defaultLocale:'en'
  }
})
