<template>
  <div class="body">
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="http://localhost:8080/">Cinema</a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost:8080/">Movies</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <br/>
    <br/>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>Thank you for your order!</h1>
                <h3>We've sent an order confimation on your email.</h3>
            </div>
        </div>
    </div>
    <!-- Footer -->
    <!-- <div class="container my-5"> -->
    <footer style="background-color: #deded5; position: fixed; bottom: 0; width: 100%;">
      <div class="container p-4">
        <div class="row">
          <div class="col-lg-6 col-md-12 mb-4">
            <h5 class="mb-3" style="letter-spacing: 2px; color: #818963;">footer content</h5>
            <p>
              This is one of the best movie rental sites in the world. Movie rental may be a bit old school, but that just makes it more special. This is vital information and totally not space filling text.
            </p>
          </div>
          <div class="col-lg-3 col-md-6 mb-4">
            <h5 class="mb-3" style="letter-spacing: 2px; color: #818963;">links</h5>
            <ul class="list-unstyled mb-0">
              <li class="mb-1">
                <a href="http://localhost:8080/#/locations" style="color: #4f4f4f;">Pickup Locations</a>
              </li>
            </ul>
          </div>
          <div class="col-lg-3 col-md-6 mb-4">
            <h5 class="mb-1" style="letter-spacing: 2px; color: #818963;">opening hours</h5>
            <table class="table" style="color: #4f4f4f; border-color: #666;">
              <tbody>
                <tr>
                  <td>Mon - Fri:</td>
                  <td>8am - 9pm</td>
                </tr>
                <tr>
                  <td>Sat - Sun:</td>
                  <td>8am - 1am</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
        © 2022 Copyright:
        <a class="text-dark" href="#">MovieRenting</a>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Movies',
  data () {
    return {

    }
  },
  mounted () {

  }
}
</script>

<style>
</style>
