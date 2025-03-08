import { Client } from 'ts-postgres';

export class DatabaseService {
    private client: Client;

    constructor() {
        this.client = new Client({
            host: 'localhost',
            port: 5432,
            database: 'your_database',
            user: 'your_user',
            password: 'your_password'
        });
    }

    async connect(): Promise<void> {
        try {
            await this.client.connect();
            console.log('Connected to the database');
        } catch (error) {
            console.error('Failed to connect to the database', error);
            throw error;
        }
    }

    async disconnect(): Promise<void> {
        try {
            await this.client.end();
            console.log('Disconnected from the database');
        } catch (error) {
            console.error('Failed to disconnect from the database', error);
            throw error;
        }
    }

    async query(queryText: string, params?: any[]): Promise<any> {
        try {
            const result = await this.client.query(queryText, params);
            return result.rows;
        } catch (error) {
            console.error('Query failed', error);
            throw error;
        }
    }
}