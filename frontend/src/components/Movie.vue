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
        <div class="col-4">
          <img :src="movie.photo" class="card-img-top" alt="">
        </div>
        <div class="col-8" style="text-align:left;">
          <h1>{{movie.title}}</h1>
          <hr/>
          <h6>{{movie.description}}</h6>
          <hr/>
          <p>You can choose to have the movie delivered to your home or you can pick it up at the rental location. (Delivery fee is $5)</p>
          <div class="form-check">
            <input v-on:click="isHidden = !isHidden" class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
              Deliver home
            </label>
          </div>
          <form v-if="!isHidden">
            <div class="form-group">
              <label for="exampleInputEmail1">Address</label>
              <input v-model="addr" type="text" class="form-control">
              <small id="emailHelp" class="form-text text-muted">This is where we'll deliver the movie</small>
            </div>
          </form>
          <hr/>
          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">Email</label>
              <input v-model="email" type="email" class="form-control">
              <small id="emailHelp" class="form-text text-muted">We need this to confirm the rental</small>
            </div>
          </form>
          <br/>
          <button v-on:click="rentMovie()" class="btn btn-primary">Rent</button>
        </div>
      </div>
    </div>
    <br/>
    <br/>
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
      movie: Object,
      isHidden: true,
      email: String,
      addr: String
    }
  },
  mounted () {
    this.email = ''
    this.addr = ''
    this.$http.get('http://127.0.0.1:8000/api/movies/?search=' + this.$route.params.title).then(res => {
      this.movie = res.data[0]
    })
  },
  methods: {
    rentMovie: function () {
      const data = {email: this.email}
      this.$http.post('http://127.0.0.1:8000/api/movies/confirmation', data)
      this.$router.push({'path': 'confirmation'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
