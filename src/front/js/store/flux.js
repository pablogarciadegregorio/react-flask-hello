import axios from "axios";

const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			token:"",
			auth:false
		},
		actions: {
			// Use getActions to call a function within a fuction

			login: async (dataEmail,dataPassword) => {
				//sincronismo y asincronismo
				try {
					//codigo exitoso
					let data = await axios.post('https://redesigned-space-computing-machine-9pq76jx54wxf9pjx-3001.app.github.dev/api/login',{
						email:dataEmail,
						password:dataPassword
					})
					// let data = await response.json();
					console.log(data);
					console.log(data.data.acess_token);
					localStorage.setItem("token", data.data.acess_token)
					setStore({auth:true})
					return true;
				} catch (error) {
					//manejar los errrores
					console.log(error);
					return false;
				}
			},


			
			getProfile: async () => {
				let token = localStorage.getItem("token")
		
				try {
					//codigo exitoso
					let data = await axios.get('https://redesigned-space-computing-machine-9pq76jx54wxf9pjx-3001.app.github.dev/api/profile',{
						headers:{
							"Authorization": `Bearer ${token}`,
						}
					})
					// let data = await response.json();
					console.log(data);
					// localStorage.setItem("token",data.data.access_token)
					setStore({auth:true})
					return true;
				} catch (error) {
					//manejar los errrores
					console.log(error);
					setStore({auth:false})
					return false;
				}
			},
			logout: () => {
				localStorage.removeItem("token")
				return false
			},
			

			validToken: async () => {
				let token = localStorage.getItem("token")
		
				try {
					//codigo exitoso
					let data = await axios.get('https://redesigned-space-computing-machine-9pq76jx54wxf9pjx-3001.app.github.dev/api/profile',{
						headers:{
							"Authorization": `Bearer ${token}`,
						}
					})
					console.log(data);
			
					return true;
				} catch (error) {
					//manejar los errrores
					console.log(error);
					return false;
				}
			},
			
			
			
			
			



// ###############################################################

			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},
			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}





		}
	};
};

export default getState;
