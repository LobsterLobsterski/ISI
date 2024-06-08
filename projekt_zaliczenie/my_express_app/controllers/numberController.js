import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const getAddNumbersForm = (req, res) => {
    res.sendFile(path.join(__dirname, '../views', 'add_numbers.html'));
};

export const addNumbers = (req, res) => {
    const num1 = parseInt(req.body.num1);
    const num2 = parseInt(req.body.num2);
    const result = num1 + num2;
    res.send(`The result is ${result}`);
};
