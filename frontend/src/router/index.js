import Vue from 'vue'
import Router from 'vue-router'
import Movies from '@/components/Movies'
import Movie from '@/components/Movie'
import Conf from '@/components/Conf'
import Locations from '@/components/Locations'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Movies',
      component: Movies
    },
    {
      path: '/confirmation',
      name: 'confirmation',
      component: Conf
    },
    {
      path: '/locations',
      name: 'locations',
      component: Locations
    },
    {
      path: '/:title',
      name: 'Movie',
      component: Movie
    }
  ]
})
