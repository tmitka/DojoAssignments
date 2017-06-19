var express = require('express');
var path = require("path");

var app = express();
var mongoose = require('mongoose');
var bodyParser = require('body-parser');

mongoose.connect('mongodb://localhost/interest');

var Schema = mongoose.Schema;




var userSchema = new Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
  interests: [{ type: Schema.Types.ObjectId, ref: 'Interests' }]
}, { timestamps: true });


var interestSchema = new Schema({
  type: { type: String, required: true },
  _user: { type: Schema.Types.ObjectId, ref: 'Users' },
}, { timestamps: true });


mongoose.model('Users', userSchema);
var Users = mongoose.model('Users');

mongoose.model('Interests', interestSchema);
var Interests = mongoose.model('Interests');

mongoose.Promise = global.Promise;

app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

app.get('/', function (request, response) {

  // get all interests
  Interests.find({}, function (err1, interests) {
    if (err1) {
      console.log(err1);
      response.render("index", { interests: [], users: [], errors: err1 });
    } else {

      // get all users with the associated interests
      Users.find({}).populate('interests').exec(function (err2, users) {
        if (err2) {
          console.log(err2);
          response.render("index", { interests: interests, users: [], errors: err2 });
        } else {
          response.render("index", { interests: interests, users: users, errors: [] });
        }
      });
    }
  })
})

app.post('/submit', function (req, res) {
  console.log("POST DATA", req.body);

  // get one user with the id in the request
  Users.findOne({ _id: req.body.user }, function (err1, user) {
    if (err1) {
      console.log(err1)
      res.redirect('/');
    } else {

      // get one interest with the id in the request
      Interests.findOne({ _id: req.body.interest }, function (err2, interest) {
        if (err2) {
          console.log(err2)
          res.redirect('/');
        } else {

          interest._user = user._id;

          console.log('interest');
          console.log(interest);

          // save the interest with the changes
          interest.save(function (err3) {
            if (err3) {
              console.log(err3);
                  res.redirect('/');
            } else {
              user.interests.push(interest);
              
              console.log('user');
              console.log(user);

              // save the user with the changes
              user.save(function (err4) {
                if (err4) {
                  console.log('err4');
                  res.redirect('/');
                } else {
                  console.log('success');
                  res.redirect('/');
                }
              })
            }
          })
        }
      })
    }
  })
})

app.listen(8000, function () {
  console.log("listening on port 8000");
});