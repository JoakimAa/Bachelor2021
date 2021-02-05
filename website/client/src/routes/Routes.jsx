/* eslint-disable react/prop-types */
import React, { Suspense } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import NoMatch from '../components/NoMatch';
import MainLayout from '../layouts/MainLayout';
import HomePage from '../pages/HomePage';
import UploadPage from '../pages/UploadPage';

const Routes = () => (
  <Router>
    <MainLayout>
      <Suspense fallback={<div>Loading ...</div>}>
        <Switch>
          <Route exact path="/home">
            <HomePage />
          </Route>
          <Route exact path="/upload">
            <UploadPage />
          </Route>
          <Route path="*">
            <NoMatch />
          </Route>
        </Switch>
      </Suspense>
    </MainLayout>
  </Router>
);

export default Routes;
