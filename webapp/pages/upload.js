import { Button, CardTitle, CardText, Container, Form } from 'reactstrap';
import { Card, Grid, Divider, Row } from '@nextui-org/react';
import Head from 'next/head'
import styles from '../styles/About.module.css';
import { useState } from 'react';

export default function Home() {
  const [stat, setState] = useState('');
  const onFileChangeHandler = (e) => {
    e.preventDefault();
    this.setState({
      selectedFile: e.target.files[0]
    });
    const formData = new FormData();
    formData.append(file, this.stat.selectedFile);
    fetch('/upload', {
      method: 'post',
      body: formData
    }).then(res => {
      if (res.ok) {
        console.log(res.data)
      }
    });
  };

  return (
    <div className=""> <Head>
      <title>iReuse: Upload</title>
      <meta name="description" content="Upload your file to iReuse"/>
      <link rel="icon" href="/favicon.ico" />
    </Head>
      <div className={styles.banner}>
        Upload
      </div>
      <Container fluid xl>
        <Grid.Container gap={2}>
          <Grid sm={12} md={5}>
            <Card css={{ mw: "330px" }}>
              <CardTitle tag="h5">
                Upload File
              </CardTitle>
              <Divider />
              <CardText>
                Uplod your image to scan it and get possible ways to reuse it.
              </CardText>
              <Divider />
              <Card.Footer>
                <Row justify="flex-end">
                  <output id="list"></output><input id="files" multiple name="files[]" type="file" accept="image/*" onChange={onFileChangeHandler} />
                  <Button type="submit" size="m">Submit</Button>
                </Row>
              </Card.Footer>
            </Card>
          </Grid>
        </Grid.Container>
      </Container>
    </div>)
}
