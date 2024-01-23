import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";
import styles from "../styles/NavBar.module.css";
import { NavLink } from "react-router-dom";

const NavBar = () => {
  return (
    <Navbar className={styles.NavBar} expand="md" fixed="top">
      <Container>
        <NavLink to="/">
          <Navbar.Brand className={styles.Logo}>
            Frag<i className="fas fa-rocket"></i>Tube
          </Navbar.Brand>
        </NavLink>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto">
            <NavLink
              exact
              to="/"
              className={styles.Link}
              activeClassName={styles.Active}
            >
              <i className="fas fa-home"></i> Home
            </NavLink>
            <NavLink
              to="/login"
              className={styles.Link}
              activeClassName={styles.Active}
            >
              <i className="fas fa-sign-in-alt"></i> Log in
            </NavLink>
            <NavLink
              to="/signup"
              className={styles.Link}
              activeClassName={styles.Active}
            >
              <i className="fas fa-user-plus"></i> Sign up
            </NavLink>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
