import { Button } from '@nextui-org/react';
import Head from 'next/head'
import styles from '../styles/Home.module.css'

const phrases = ["To save the Earth", "Avoid Global Warming", "To Reduce Waste"]

export default function Home() {
  return (
    <div> <Head>
      <title>iReuse</title>
      <meta name="description" content="Generated by create next app" />
      <link rel="icon" href="/favicon.ico" />
    </Head>
      <h1 className={styles.h1}>Why iReuse?</h1>
      <h2 className={styles.h2}>I reuse, {phrases[Math.floor(Math.random() * phrases.length)]}</h2>
      <div className={styles.grid}>
        <iframe title='Tons of waste dumped' font-size='40' src='https://www.theworldcounts.com/embed/challenges/104?background_color=white&color=black&font_family=%22Helvetica+Neue%22%2C+Arial%2C+sans-serif&font_size=14'></iframe>
      </div>
      <div className={styles.button_grid}>
        <a href="/upload">
          <Button className={styles.button} id='uploadredirect' shadow type="primary" size="xl">Upload Your Image!</Button>
        </a>
      </div>
    </div>)
}
