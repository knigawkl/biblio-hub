let login = Math.random().toString(36).substring(2, 15);

describe('Register', function() {
  it('visit bibliohub', function () {
    cy.visit('http://localhost:8081/')
  });

  it('click Sign Up', function () {
    cy.contains('Sign up').click();
  });

  it('enter email', function () {
    cy.get('#reg_email').type('test@mail.com');
  });

  it('enter login', function () {
    cy.get('#reg_login').type(login);
  });

  it('enter password', function () {
    cy.get('#reg_password').type('pass');
  });

  it('click register', function () {
    cy.contains('Register').click();
  });
});

describe('Login', function() {
  it('enter login', function () {
    cy.get('#login').type(login);
  });

  it('enter password', function () {
    cy.get('#password').type('pass');
  });

  it('click sign in', function () {
    cy.get('.btn-dark').click();
  });

  it('check current url', function () {
    cy.url().should('eq', 'http://localhost:8081/#/hub')
  });
});

describe('Logout and login', function() {
  it('logout', function () {
    cy.contains('Log out').click();
  });

  it('login', function () {
    cy.get('#login').type(login);
    cy.get('#password').type('pass');
    cy.get('.btn-dark').click();
  });

  it('check current url', function () {
    cy.url().should('eq', 'http://localhost:8081/#/hub')
  });
});

describe('Add a new book', function() {
  it('open add book popup', function () {
    cy.contains('Add Book').click();
  });

  
});