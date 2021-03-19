import React from 'react';
import styled from 'styled-components';
import Nav from '../components/Nav';

const StyledHeader = styled.header`
  background: #fff;
  box-shadow: 1px 1px 2px #f5f5f5;
  margin-bottom: 60px;
`;

const Wrapper = styled.section`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

// eslint-disable-next-line react/prop-types
const MainLayout = ({ children }) => (
  <>
    <StyledHeader>
      <Nav />
    </StyledHeader>
    <Wrapper>{children}</Wrapper>
  </>
);

export default MainLayout;
