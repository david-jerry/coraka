// This is the scss entry file
import "../styles/index.scss";
import 'flowbite';
import htmx from "htmx.org/dist/htmx";
import Alpine from "alpinejs";

// We can import other JS file as we like
import "../components/sidebar";

// initialize htmx
window.htmx = htmx;
// initialize ether js for crypto payment
// window.ethers = ethers;
// initialize axios async post|get request
// window.axios = axios;

window.Alpine = Alpine;
// Alpine.data("web3Functions", web3Functions);
// Alpine.data("signup", signup);
Alpine.start();

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
});
