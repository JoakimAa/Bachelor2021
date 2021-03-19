import React from 'react';
import { ThemeProvider, CSSReset } from '@chakra-ui/core';
import Routes from './src/routes/Routes';
import customTheme from './src/styles/theme';

const App = () => (
  <ThemeProvider theme={customTheme}>
    <CSSReset />
    <Routes />
  </ThemeProvider>
);

export default App;
