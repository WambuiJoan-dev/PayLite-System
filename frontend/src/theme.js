import { createTheme } from '@mui/material/styles';
import { blue, grey } from '@mui/material/colors';

// Create a theme instance.
const theme = createTheme({
  palette: {
    primary: {
      main: blue[700],
    },
    secondary: {
      main: grey[500],
    },
    background: {
      default: grey[50],
    },
  },
});

export default theme;