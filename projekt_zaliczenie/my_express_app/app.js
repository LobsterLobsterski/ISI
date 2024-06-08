import express from 'express';
import bodyParser from 'body-parser';
import path from 'path';
import { fileURLToPath } from 'url';

import sequelize from './config/database.js';
import { addUser, getUsers } from './controllers/userController.js';
import { getPhotos } from './controllers/photoController.js';
import { getName } from './controllers/nameController.js';
import { getAddNumbersForm, addNumbers } from './controllers/numberController.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.post('/add_user', addUser);
app.get('/users', getUsers);

app.get('/my_name', getName);

app.get('/add_numbers', getAddNumbersForm);
app.post('/add_numbers', addNumbers);

app.get('/photos', getPhotos);

sequelize.sync().then(() => {
    app.listen(3000, () => {
        console.log('Server is running on http://localhost:3000');
    });
});
