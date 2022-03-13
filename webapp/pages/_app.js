import '../styles/globals.css'
import 'bootstrap/dist/css/bootstrap.css';
import { NextUIProvider, createTheme } from '@nextui-org/react';
import NavBar from '../components/NavBar'
const theme = createTheme({
  type: "light",
  theme: {
    colors: {
      // brand colors
      primaryLight: '#FF79C6',
      primary: '#FF79C6',
      primaryDark: '#FF79C6',

      gradient: 'linear-gradient(112deg, $blue100 -25%, $pink500 -10%, $purple500 80%)',
      link: '#5E1DAD',

      // you can also create your own color
      myColor: '#ff4ecd'

      // ...  more colors
    },
    space: {},
    fonts: {}
  }
})
function MyApp({ Component, pageProps }) {
  return (<NextUIProvider theme={theme}>

    <NavBar />
    <Component {...pageProps} />
  </NextUIProvider>

  )
}

export default MyApp
