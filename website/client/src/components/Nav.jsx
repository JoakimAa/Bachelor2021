import React from 'react';
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

const Nav = () => (
  <Wrapper>
    <Header>
      <H1Text>Bachelor 2021</H1Text>
      <NavBar2>
        <UnorderedList>
          <ListItem>
            <NavLink exact to="/home" activeClassName="active">
              Hjem
            </NavLink>
          </ListItem>
          <ListItem>
            <NavLink exact to="/upload" activeClassName="active">
              Send inn
            </NavLink>
          </ListItem>
        </UnorderedList>
      </NavBar2>
    </Header>
  </Wrapper>
);

const UnorderedList = styled.ul`
  margin: 0;
  display: inline;
  padding-right: 0.15em;
`;

const ListItem = styled.li`
  & a {
    font-weight: bold;
  }

  & a.active,
  a:hover {
    color: #2c91bd;
  }

  display: inline-block;
  list-style: none;
  padding: 0.36em 0.9375em;

  & > a {
    text-decoration: none;
  }
`;

const Wrapper = styled.div`
  width: 100%;
  margin: 0 auto;
`;

const H1Text = styled.h1`
  font-weight: bold;
  display: inline;
  margin: 0 0 0 4rem;
  font-size: 3rem;
`;

const Header = styled.header`
  background-color: white;
  box-shadow: 0 6px 4px -2px rgba(0, 0, 0, 0.2);
  padding: 0.35em;
  width: 100%;
  display: inline-block;
`;

const NavBar2 = styled.nav`
  float: right;
  font-size: 1.5em;
`;

export default Nav;
