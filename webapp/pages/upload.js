import { Button, CardTitle, CardText, Container, Form } from 'reactstrap';
import { Card, Grid, Divider, Row } from '@nextui-org/react';
import Head from 'next/head'
import styles from '../styles/About.module.css';
import React, { useState } from 'react';

export default function Home() {
  let fileInput = React.createRef();
  const onSubmitHandler = (e) => {
    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);
    fetch('http://localhost:5000/uploadfile', {
    method: 'POST',
    body: formData
    }).then(resp => console.log(resp)).catch(e=> console.log('err'));

  }

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
                  <form>
                  <output id="list"></output><input id="files" multiple name="files[]" type="file" accept="image/*" ref={fileInput}  />
                  <Button type="submit" size="m"   onClick={onSubmitHandler}
>Submit</Button>
                  </form>
                </Row>
              </Card.Footer>
            </Card>
          </Grid>
        </Grid.Container>
      </Container>
    </div>)
}
