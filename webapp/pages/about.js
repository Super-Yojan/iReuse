import Head from 'next/head'
import styles from '../styles/About.module.css';

export default function Home() {
  return (
    <div> <Head>
      <title>iReuse: About</title>
        <meta name="description" content="About iReuse" />
      <link rel = "icon" href = "/favicon.ico" />
      </Head>
      <div className={styles.banner}>
        About US
      </div>
      <p>
        We are iReuse
      </p>


    </div>)
}
