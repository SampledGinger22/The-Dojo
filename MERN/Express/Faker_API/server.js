const express = require("express");
const app = express();
const { faker } = require("@faker-js/faker");
const port = 8000;

const User = () => {
  const newUser = {
    firstName: faker.name.firstName(),
    lastName: faker.name.lastName(),
    email: faker.internet.email(),
    phoneNumber: faker.phone.phoneNumber(),
    password: faker.internet.password(),
    _id: faker.datatype.uuid()
  };
  return newUser;
}

const Company = () => {
  const newCompany = {
    _id: faker.datatype.uuid(),
    name: faker.company.companyName(),
    address: {
      street: faker.address.streetAddress(),
      city: faker.address.cityName(),
      state: faker.address.state(),
      zipCode: faker.address.zipCode(),
      country: faker.address.country()
    }
  }
  return newCompany;
}


// req is short for request
// res is short for response
app.get("/api/users/new", (req, res) => {
  res.send(newUser);
});

app.get("/api/companies/new", (req, res) => {
  res.send(newCompany);
});

app.get("/api/user/company", (req, res) => {
  res.send(newUser, newCompany);
});

// const server = app.listen(8000, () =>
//   console.log(`Server is locked and loaded on port ${server.address().port}!`)
// );
