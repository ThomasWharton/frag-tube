 // IMPORTANT!!
 // Because this React app is running in the same workspace as the API,

 // there is no need to set a separate baseURL until you reach deployment.

 // Setting a baseURL before you reach deployment will cause errors
import axios from "axios";

axios.defaults.baseURL = "https://8000-thomaswharton-fragtube-znmj52ekm2k.ws-eu107.gitpod.io";
axios.defaults.headers.post['Content-Type'] = 'multipart/form-data'
axios.defaults.withCredentials = true;

