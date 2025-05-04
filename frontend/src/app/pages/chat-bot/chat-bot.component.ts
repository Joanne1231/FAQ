
import { Component } from '@angular/core'
import { HttpClient, HttpClientModule } from '@angular/common/http'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { MatButtonModule } from '@angular/material/button'
import { MatCardModule } from '@angular/material/card'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatIconModule } from '@angular/material/icon'


@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    MatButtonToggleModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatButtonModule,
  ],
  templateUrl: './chat-bot.component.html',
  styleUrls: ['./chat-bot.component.scss'],
})
export class ChatBotComponent {
  faqData: any[] = []
  suggestedFaqs: any[] = []
  selectedCategory = 'service'
  // 顯示使用者選擇的問題或輸入的問題
  selectedQuestion: string | null = null
  // 顯示機器人回應的內容
  botResponse: string | null = null
  userInput = ''

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get<any[]>('/api/faqs/init').subscribe({
      next: data => {
        console.info(data, '載入 FAQ 資料')
        this.faqData = data
        this.updateSuggestions(this.selectedCategory)
      },
      error: (error) => {
        console.error(error, '無法載入 FAQ 資料')
        this.faqData = [];
      }
    })
  }

  updateSuggestions(category: string) {
    this.suggestedFaqs = this.faqData
      .filter(faq => faq.category === category).slice(0, 5);
  }

  onSelectFaq(faq: { question: string }) {
    this.selectedQuestion = faq.question
    this.sendToBot(faq.question)
  }
  onSubmit() {
    if (!this.userInput.trim()) return;
    this.selectedQuestion = this.userInput;
    this.sendToBot(this.userInput);
    this.userInput = '';
  }
  /**
   * 處理輸入欄位的 keydown 事件。
   * 
   * 如果按下 Enter 鍵且未同時按下 Shift，則會阻止預設行為（例如換行），
   * 並呼叫 `onSubmit()` 進行送出。
   * 
   * @param event - 使用者輸入時觸發的鍵盤事件。
   */
  onInputKeydown(event: KeyboardEvent) {
    if ('key' in event && event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.onSubmit();
    }
  }
  /**
   * 發送使用者的問題到聊天機器人 API，並更新機器人回應。
   *
   * @param question - 使用者要發送給聊天機器人的問題。
   * 
   * 將 `this.botResponse` 設為 API 回傳的答案，若請求失敗則顯示錯誤訊息。
   */
  sendToBot(question: string) {
    this.botResponse = null
    this.http
      .post<{ answer: string }>('/api/chat', { question })
      .subscribe({
        next: res => (this.botResponse = res.answer),
        error: () => (this.botResponse = '暫時無法回應，請稍後再試。'),
      })
  }

  /** 切換toggle */
  onCategoryChange(category: string) {
    console.log('Selected category:', category)
    this.selectedCategory = category;
    this.updateSuggestions(category);


  }


}
