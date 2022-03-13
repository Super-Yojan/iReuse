import Head from 'next/head'
import styles from '../styles/About.module.css';

export default function Home() {
  return (
    <div> <Head>
      <title>iReuse: About</title>
      <meta name="description" content="About iReuse" />
      <link rel="icon" href="/favicon.ico" />
    </Head>
      <div className={styles.banner}>
        <h1>About US</h1>
        <h3>We are iReuse:</h3>
      </div>
      <p className={styles.para}>
        We are a group of freshmen college students at George Mason University who are interested in Computer Science and keeping our Earth clean. We decided to use our technical skills to help people find creative ways to reuse objects that would otherwise end up in despicable landfills. Every year we dump a massive 2.12 billion tons of waste. If all this waste was put on trucks they would go around the world 24 times. This stunning amount of waste is partly because 99 percent of the stuff we buy is trashed within 6 months. Our goal is to use the power of creativity to encourage our peers to help reduce the amount waste on our planet.
      </p>
    </div>)
}
