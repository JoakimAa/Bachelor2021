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
  @media (min-width: 200px) and (max-width: 500) {
    padding: 0.1em;
    justify-content: center;
    display: flex;
  }

  @media (min-width: 501px) and (max-width: 800px) {
    margin: 0;
    padding: 0;
  }

  @media (min-width: 801px) {
    margin: 0;
    display: inline;
    padding-right: 0.15em;
  }
`;

const ListItem = styled.li`
  @media (min-width: 200px) and (max-width: 500) {
    background-color: white;
    border-radius: 1em;
    margin-top: 1em;
    padding: 0.6em;
    list-style: none;

    & > a {
      padding: 1em;
      text-decoration: none;
    }
  }

  @media (min-width: 501px) and (max-width: 800px) {
    display: inline;

    & > a {
      display: inline-block;
      padding: 1em;
      text-decoration: none;
    }
  }

  @media (min-width: 801px) {
    display: inline-block;
    list-style: none;
    padding: 0.36em 0.9375em;

    & > a {
      text-decoration: none;
    }
  }
`;

const Wrapper = styled.div`
  width: 100%;
  margin: 0 auto;
`;

const H1Text = styled.h1`
  font-weight: bold;

  @media (min-width: 200px) and (max-width: 500px) {
    margin-top: 0;
    padding: 0.25em;
    font-size: 2rem;
    text-align: center;
  }

  @media (min-width: 501px) and (max-width: 800px) {
    margin-top: 0;
    padding: 0.3em;
    font-size: 2rem;
    text-align: center;
  }

  @media (min-width: 801px) {
    display: inline;
    margin: 0 0 0 4rem;
    font-size: 3rem;
  }
`;

const Header = styled.header`
  background-color: white;
  box-shadow: 0 6px 4px -2px rgba(0, 0, 0, 0.2);

  @media (min-width: 801px) {
    padding: 0.35em;
    width: 100%;
    display: inline-block;
  }
`;

const NavBar2 = styled.nav`
  @media (min-width: 200px) and (max-width: 500) {
    font-size: 1.3em;
    margin-right: 2.9em;
    margin-left: 2.9em;
    padding: 0;
    text-align: center;
    text-decoration: none;
  }

  @media (min-width: 501px) and (max-width: 800px) {
    background-color: white;
    font-size: 1.4em;
    margin: 0;
    padding: 0;
    text-align: center;
  }

  @media (min-width: 801px) {
    display: inline-block;
    float: right;
    font-size: 1.5em;
  }
`;

export default Nav;
