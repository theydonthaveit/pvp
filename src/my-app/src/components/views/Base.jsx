import React from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Home from './Home'
import Dashboard from './Dashboard'

const Base = () => (
    <Router>
        <div>
            <Link to="/">Home</Link>
            <Link to="/dashboard">Dashboard</Link>

            <Route exact path="/" component={Home} />
            <Route path="/dashboard" component={Dashboard} />
        </div>
    </Router>
)

export default Base