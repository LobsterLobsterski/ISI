import User from '../models/user.js';

export const addUser = async (req, res) => {
    const { name, email } = req.body;
    try {
        const user = await User.create({ name, email });
        res.json({ message: 'User added successfully!', user });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

export const getUsers = async (req, res) => {
    const users = await User.findAll();
    res.json(users);
};
