import { Button, CardTitle, CardText, Container, Form } from 'reactstrap';
import { Card, Grid, Divider, Row } from '@nextui-org/react';
import Head from 'next/head'
import styles from '../styles/About.module.css';
import React, { useState } from 'react';
import axios from 'axios';

export default function Home() {
   const [options, setOptions] = useState();
   const fileInput = React.useRef();
   const onSubmitHandler = async (e) => {
     e.preventDefault();
    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);
    await axios.post('http://localhost:5000/uploadfile', formData,{ 
    headers: {
      'Content-Type': 'multipart/form-data'
    }
    }).then(resp => {console.log(typeof resp.data);
      setOptions(resp.data['options']);
      console.log(options);
    }).catch(error => {console.log(error)})

     

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
                  <form  onSubmit={onSubmitHandler}>
                  <output id="list"></output><input id="files" name="file" type="file" accept="image/*" ref={fileInput}   />
                    <Button type="submit" size="m">Submit</Button>
                  </form>
                </Row>
              </Card.Footer>
            </Card>
          </Grid>
        </Grid.Container>
      </Container>
      <Container>
        {
          options?options.map(x=>(<Card><CardText>{x.desc}</CardText><Card.Footer>{x.url}</Card.Footer></Card>)): ''
        }
     </Container>
    </div>)
}
