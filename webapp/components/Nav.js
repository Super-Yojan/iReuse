import { Col, Container, Row ,Button} from "@nextui-org/react";


export default function Nav(){

  return(
    <Container fluid>
      <Row>
        <Col>
          iReuse
          </Col>
        <Col>
          <Button>
          Home
            </Button>
          </Col>
        <Col>
          About
        </Col>
        <Col>
          Search
          </Col>
        </Row>


      </Container>


  )

}
