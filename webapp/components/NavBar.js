import {Navbar, Nav,NavItem, NavLink, NavbarBrand, NavbarToggler, Collapse} from 'reactstrap';

export default function NavBar() {

  return (
        <Navbar
    color="light"
    expand="md"
    light
  >
    <NavbarBrand href="/">
      iReuse
    </NavbarBrand>
    <NavbarToggler onClick={function noRefCheck(){}} />
    <Collapse navbar>
      <Nav
        className="ms-auto "
        navbar
      >
        <NavItem>
          <NavLink href="/">
            Home
          </NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="/about">
            About
          </NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="/upload">
            Upload
          </NavLink>
        </NavItem>
      </Nav>
   
    </Collapse>
  </Navbar>)
}
