<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    
  </div>
</template>

<script>
const SECRET_NUM = 'Secretkey'
    var jwt = require('jsonwebtoken');
    var token = jwt.sign({username: 'Farhana', password: "123"}, SECRET_NUM);
    // eslint-disable-next-line no-console
    console.log(token)

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
       
    }
  },
  created() {
            fetch("http://127.0.0.1:8000/api/student/", {
                method: 'GET', 
                
                headers: {
                    Authorization:token,
                    'Content-Type': 'application/json',
                    // 'Access-Control-Allow-Origin': true
                    // 'Content-Type': 'application/x-www-form-urlencoded',
                },
            })
                .then((response) => {
                    return response
                }).then((data) => {
                // eslint-disable-next-line no-console
                console.log(data)
            })
        
          //  fetch('https://jsonplaceholder.typicode.com/todos/1')
          //   .then(response => response.json())
          //   .then(json => console.log(json)) 
  }     
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
