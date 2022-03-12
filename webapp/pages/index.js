import {Button} from '@nextui-org/react';
import Head from 'next/head'

export default function Home() {
  return (
    <div> <Head>
        <title>iReuse</title>
        <meta name="description" content="Generated by create next app" />
      <link rel = "icon" href = "/favicon.ico" />
      </Head>
      <Button type = "primary">Primary Button</Button>
    </div>)
}
