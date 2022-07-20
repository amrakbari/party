import React, { Component } from 'react'
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";


export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        console.log('test22')
        return (
            <Router>
                <Routes>
                    <Route exact path="/" element={<p>this is home page</p>}/>
                    <Route path="/join" element={<RoomJoinPage />} />
                    <Route path="/create" element={<CreateRoomPage />} />
                </Routes>
            </Router>
        );
    }
}