/**
 * Preloader
 */
let preloader = document.querySelector("#preloader");
if (preloader) {
  window.addEventListener("load", () => {
    preloader.remove();
  });
}
/**
 * Nav Notification
 */
$(function () {
  $('[data-tooltip="tooltip"]').tooltip();
});
