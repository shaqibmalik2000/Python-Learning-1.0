import './App.css';
import { Navbar, Container, Nav, NavDropdown, Row, Col, Image, Button, Card } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="App">
      <header>
      <Navbar className='bg-body-tertiary' bg="dark" data-bs-theme="dark" expand="lg">
      <Container>
        <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#link">Link</Nav.Link>
            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Another action
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Separated link
              </NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
      </header>
      <main>
        <containter>
        <Row className="px-4 my-5">
        <Col sm={7}>
        <Image 
          src="https://dummyimage.com/900x400/dee2e6/6x757d.jpg" 
          fluid 
          rounded
          className=""
        />
        </Col>
        <Col sm={5}>
         <h1 class="font-weigh-light">Tagline</h1>
         <p>This is a great template for small businesses.
          </p>
          <Button> Call to action</Button> 
        </Col>
      </Row>
      <row>
        <card className="text-center bg-secondary text-white my-5 py-4">
          <Card.Body>This is some text with a card body. A great place to showcase some important information or display a clever tagline!
          </Card.Body>
        </card>
      </row>
      <row>
        <Col>

        </Col>
      </row>
        </containter>
      </main>
    </div>
  );
}

export default App;
