import { Card, Button, CardBody, CardTitle, CardText} from 'reactstrap';
import Head from 'next/head'
import styles from '../styles/About.module.css';

export default function Home() {
  return (
    <div> <Head>
      <title>iReuse: Upload</title>
        <meta name="description" content="Upload your file to iReuse" />
      <link rel = "icon" href = "/favicon.ico" />
      </Head>
      <div className={styles.banner}>
        Upload

      </div>

      <Card>
    <CardBody>
      <CardTitle tag="h5">
        Upload File
      </CardTitle>
      
      <CardText>
        Uplod your image to scan it and get possible ways to reuseit.
      </CardText>
    <output id="list"></output><Button><input id="files" multiple name="files[]" type="file" /></Button>

    </CardBody>
        </Card>


    </div>)
}
