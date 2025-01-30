import axios from 'axios';
import { API_URL } from '../config';

export async function sendRowToKafka(row: Record<string, any>): Promise<void> {
  try {
    await axios.post(`${API_URL}/send`, row);
  } catch (error) {
    throw new Error('Failed to send row to Kafka.');
  }
}
