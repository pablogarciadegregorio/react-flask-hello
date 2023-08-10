import React , {useContext}from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";



export const Navbar = () => {
	const { store, actions } = useContext(Context);
	const navigate = useNavigate();

	function handleLogout() {
		let logged = actions.logout()
		if (!logged) {
			navigate("/login")
		}
	}

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					{/* <Link to="/demo"> */}
						<button className="btn btn-primary" onClick={handleLogout}>LOGOUT</button>
					{/* </Link> */}
				</div>
			</div>
		</nav>
	);
};
