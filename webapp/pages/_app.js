import '../styles/globals.css'
import 'bootstrap/dist/css/bootstrap.css';
import {NextUIProvider} from '@nextui-org/react';
import NavBar from '../components/NavBar'
function MyApp({Component, pageProps}) {
  return (<NextUIProvider>

      <NavBar/>
    <Component { ...pageProps } />
    </NextUIProvider>

  )
}

export default MyApp
